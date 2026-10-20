#include "dsp.hpp"
#include <iostream>

int main()
{
    const double powers[] = {1.0, 10.0, 100.0, 0.5};
    for (double p : powers)
    {
        std::cout << "P = " << p
                  << "  ->  " << power_to_db(p) << " dB\n";
    }
    return 0;
}
