/* file: count.c */

#include <math.h>
#include <stdlib.h>

   
int count(int n)                             /*1*/
        {
        int count_inside, count;
        double x, y;
        count_inside = 0;
        for (count=0; count < n; count++)
            {
            x = rand();
            y = rand();
            if (sqrt(x * x + y * y) < RAND_MAX)
                count_inside +=  1;
            }
        return count_inside;
        }

int main(int argc, const char* argv[])       /*2*/
{
  int n; 
  scanf("%d",&n);
  printf("%d\n", count(n));
}
