/* file: pi_read.c */

#include <math.h>
#include <stdlib.h>

   
double piC(int n)
        {
        int count_inside, count;
        double x, y, d, pi;
        count_inside = 0;
        for (count=0; count < n; count++)
            {
            x = rand();
            y = rand();
            d = sqrt(x*x + y*y);
            if (d < RAND_MAX)
                count_inside +=  1;
            }
        pi = 4.0 * count_inside / n;
        return pi;
        }

int main(int argc, const char* argv[])
{
  int n; 
  scanf("%d",&n);
  printf("%15.13f\n", piC(n));
}

        


        
        