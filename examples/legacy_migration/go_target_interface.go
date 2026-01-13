package interest

import (
	"math/big"
)

// InterestCalculator defines the interface for legacy interest migration
type InterestCalculator interface {
	Calculate(principal *big.Float, rate *big.Float, days int) (*big.Float, error)
}
