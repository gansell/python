/* file: countsleep.c */

#include <math.h>
#include <stdlib.h>
#include <windows.h>

   
int count(int n)
        {
        int count_inside, count;
        double x, y, d;
        count_inside = 0;
        for (count=0; count < n; count++)
            {
            Sleep(1);
            x = rand();
            y = rand();
            d = sqrt(x*x + y*y);
            if (d < RAND_MAX)
                count_inside +=  1;
            }
        return count_inside;
        }

int main(int argc, const char* argv[])
{
  int n; 
  scanf("%d",&n);
  printf("%d\n", count(n));
}

        


        
        