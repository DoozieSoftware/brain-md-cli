"""TOON Parser - Token-Oriented Object Notation parser."""

import re
from brain_md.models import ParseError


def parse_toon(content: str) -> dict:
    """
    Parse TOON formatted content into a dictionary.

    Handles:
    - SECTION: headers
    - key: value pairs with two-space indentation
    - # comments (stripped)
    - SECTION[n]{keys}: tabular arrays
    - >>>...<<< heredoc blocks

    Returns:
        Dictionary with section names as keys

    Raises:
        ParseError: If content is malformed
    """
    result: dict = {}
    lines = content.splitlines()

    # Strip comments first (but preserve heredoc delimiters)
    lines = strip_comments(lines)

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check for heredoc start: >>> (with or without content)
        stripped = line.strip()
        if stripped.startswith(">>>"):
            # Extract content after >>> if present
            if len(stripped) > 3:
                first_line = stripped[3:]
                if first_line:
                    heredoc_content = [first_line]
                else:
                    heredoc_content = []
            else:
                heredoc_content = []

            i += 1
            # Collect lines until closing delimiter
            while i < len(lines):
                stripped_line = lines[i].strip()
                if stripped_line == "<<<" or stripped_line.startswith("<<<"):
                    # Extract content after <<< if present
                    if len(stripped_line) > 3:
                        heredoc_content.append(stripped_line[3:])
                    # Skip closing delimiter
                    i += 1
                    break
                heredoc_content.append(lines[i])
                i += 1

            # Store heredoc content in a special section
            heredoc_key = (
                f"heredoc_{len([k for k in result.keys() if k.startswith('heredoc_')])}"
            )
            result[heredoc_key] = "\n".join(heredoc_content)
            continue

        # Skip empty lines
        if not line.strip():
            i += 1
            continue

        # Check for tabular array header: SECTION[n]{keys}:
        tabular_match = re.match(r"^([A-Z_]+)\[(\d+)\]\{([^}]+)\}:\s*$", line)
        if tabular_match:
            section_name = tabular_match.group(1)
            count = int(tabular_match.group(2))
            keys = [k.strip() for k in tabular_match.group(3).split(",")]

            # Parse the rows
            rows = []
            i += 1
            while i < len(lines) and len(rows) < count:
                row_line = lines[i]
                if not row_line.strip():
                    i += 1
                    continue
                # Row must be indented
                if row_line.startswith("  "):
                    row_values = parse_tabular_row(row_line.strip())
                    if len(row_values) == len(keys):
                        rows.append(dict(zip(keys, row_values)))
                    i += 1
                else:
                    break

            result[section_name] = rows
            continue

        # Check for section header: SECTION:
        section_match = re.match(r"^([A-Z_]+):\s*$", line)
        if section_match:
            section_name = section_match.group(1)
            section_content: dict = {}
            i += 1

            # Parse key-value pairs (two-space indented)
            while i < len(lines):
                kv_line = lines[i]
                if not kv_line.strip():
                    i += 1
                    continue
                # Must be indented with two spaces
                if kv_line.startswith("  ") and not kv_line.startswith("    "):
                    kv_match = re.match(r"^  ([a-z_][a-z0-9_]*):\s*(.+)$", kv_line)
                    if kv_match:
                        key = kv_match.group(1)
                        value = parse_value(kv_match.group(2))
                        section_content[key] = value
                        i += 1
                    else:
                        break
                else:
                    break

            result[section_name] = section_content
            continue

        # Unknown line - skip
        i += 1

    return result


def strip_comments(lines: list[str]) -> list[str]:
    """
    Remove comment lines from TOON content.

    Lines starting with # (after optional whitespace) are comments.
    Heredoc delimiters (>>>, <<<) are not treated as comments.
    """
    result = []
    for line in lines:
        stripped = line.strip()
        # Don't treat heredoc delimiters as comments
        if stripped.startswith(">>>") or stripped.startswith("<<<"):
            result.append(line)
        # Strip comment lines
        elif stripped.startswith("#"):
            continue
        else:
            result.append(line)
    return result


def parse_value(value_str: str) -> str | int:
    """
    Parse a TOON value string.

    - Quoted strings: remove quotes
    - Integers: convert to int
    - Unquoted: return as-is
    """
    value_str = value_str.strip()

    # Quoted string
    if value_str.startswith('"') and value_str.endswith('"'):
        return value_str[1:-1]

    # Try integer
    try:
        return int(value_str)
    except ValueError:
        pass

    return value_str


def parse_tabular_row(row: str) -> list[str | int]:
    """
    Parse a comma-separated row from a tabular array.

    Handles quoted values with commas inside.
    """
    values = []
    current = ""
    in_quotes = False

    for char in row:
        if char == '"':
            in_quotes = not in_quotes
            current += char
        elif char == "," and not in_quotes:
            values.append(parse_value(current.strip()))
            current = ""
        else:
            current += char

    # Don't forget the last value
    if current.strip():
        values.append(parse_value(current.strip()))

    return values


def parse_tabular_array(header: str, rows: list[str]) -> list[dict]:
    """
    Parse a tabular array into a list of dictionaries.

    Args:
        header: The header line like "SECTION[n]{key1, key2}:"
        rows: List of comma-separated value rows

    Returns:
        List of dictionaries with keys from header

    Raises:
        ParseError: If header format is invalid
    """
    match = re.match(r"^([A-Z_]+)\[(\d+)\]\{([^}]+)\}:\s*$", header)
    if not match:
        raise ParseError(f"Invalid tabular array header: {header}")

    keys = [k.strip() for k in match.group(3).split(",")]
    result = []

    for row in rows:
        row = row.strip()
        if not row:
            continue
        values = parse_tabular_row(row)
        if len(values) != len(keys):
            raise ParseError(
                f"Row has {len(values)} values but header defines {len(keys)} keys"
            )
        result.append(dict(zip(keys, values)))

    return result
