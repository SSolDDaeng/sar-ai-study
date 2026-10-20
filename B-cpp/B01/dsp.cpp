#include "dsp.hpp"
#include <cmath>  // std::log10

double power_to_db(double power)
{
    return 10.0 * std::log10(power);  // 전력 dB = 10 * log10(P)
}

