#include<stdio.h>
#include<string.h>
#include<math.h>

float means[3][2];
float mean[3][2] = {0,0,0,0,0,0};
int i;
int points[100][3];

int mins(float x,float y,float z)
{
    if(x<y && x<z)
        return 1;
    else if(y<x && y<z)
        return 2;
    else
        return 3;
}
float euclid(float x1,float y1,float x2,float y2)
{
    return (sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) ));
}

//mean is main and means is temp
void calculate_mean()
{
    float dist,dist2,dist3;
    float sum1x=0,sum1y=0,sum2x=0,sum2y=0,sum3x=0,sum3y=0,count1=0,count2=0,count3=0;
    for(i=0;i<100;i++)
    {
        dist = euclid(points[i][0],points[i][1],means[0][0],means[0][1]);
        dist2 = euclid(points[i][0],points[i][1],means[1][0],means[1][1]);
        dist3 = euclid(points[i][0],points[i][1],means[2][0],means[2][1]);
        points[i][2] = mins(dist,dist2,dist3);
    }
    for(i=0;i<100;i++)
    {
        if (points[i][2] ==1)
        {
            count1++;
            sum1x = sum1x+points[i][0];
            sum1y = sum1y +points[i][1];
        }
        if (points[i][2] ==2)
        {
            count2++;
            sum2x = sum2x+points[i][0];
            sum2y = sum2y +points[i][1];
        }
        if (points[i][2] ==3)
        {
            count3++;
            sum3x = sum3x+points[i][0];
            sum3y = sum3y +points[i][1];
        }
    }
    means[0][0] = (float)sum1x/count1;
    means[0][1] = (float)sum1y/count1;
     means[1][0] = (float)sum2x/count2;
    means[1][1] = (float)sum2y/count2;
     means[2][0] = (float)sum3x/count3;
    means[2][1] = (float)sum3y/count3;
}
int main()
{
    int x,y,ix = 0;
    char l,c,r;
    FILE *f;
    f = fopen("k-means.txt","r");
    while(!feof(f))
    {
        fscanf(f,"%c %d %c %d %c \n",&l,&x,&c,&y,&r);
        points[ix][0] = x;
        points[ix][1] = y;
        ix++;
    }
    fclose(f);
    means[0][0] = points[0][0];
    means[0][1] = points[0][1];
    means[1][0] = points[1][0];
    means[1][1] = points[1][1];
    means[2][0] = points[2][0];
    means[2][1] = points[2][1];
    while(1)
    {
        calculate_mean();
        if(means[0][0] == mean[0][0] && means[0][1] == mean[0][1] && means[1][0] == mean[1][0] && means[1][1] == mean[1][1] && means[2][0] == mean[2][0] && means[2][1] == mean[2][1])
            break;
        mean[0][0] = means[0][0];
        mean[0][1] =  means[0][1];
        mean[1][0] =  means[1][0];
        mean[1][1] =  means[1][1];
        mean[2][0] =  means[2][0];
        mean[2][1] =  means[2][1];

    }
    for(i=0;i<3;i++)
    {
        printf("the value of means is x = %f \ty = %f\n",means[i][0],means[i][1]);
    }
    return 0;
}

