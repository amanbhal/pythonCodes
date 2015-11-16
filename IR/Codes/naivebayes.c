#include<stdio.h>
#include<string.h>
#include<math.h>

int count1 = 0,count2=0;
int countpi1 = 0,countpi2 = 0;
int main()
{
    FILE *f;
    f = fopen("output.txt","r");
    int x,y,xfinal,yfinal;
    char c[2];
    char l,cc,r;
    int div,pix1,pix2,piy1,piy2;
    int xmin1,xmin2,ymin1,ymin2,xmax1,xmax2,ymax1,ymax2;
    float P1,P2,p1,p2;
    while(!feof)
    {
        fscanf(f,"%c %d %c %d %c %s\n",&l,&x,&cc,&y,&r,&c);
        if(strcmp(c,"C1")==0)
        {
            count1++;
            if(x<xmin1)
                xmin1=x;
            if(x>xmax1)
                xmax1 = x;
            if(y<ymin1)
                ymin1 = y;
            if(y>ymax1)
                ymax1 = y;
        }
         else if(strcmp(c,"C2")==0)
        {
            count2++;
            if(x<xmin2)
                xmin2=x;
            if(x>xmax2)
                xmax2 = x;
            if(y<ymin2)
                ymin2 = y;
            if(y>ymax2)
                ymax2 = y;
        }
        else
        {
            xfinal = x;
            yfinal = y;
        }

    }
    fclose(f);
    P1 = (float)count1/(count1+count2);
    P2 = (float)count2/(count1+count2);
    div = 2;
    pix1 = xfinal-xfinal%div;
    pix2 = pix1 +div;
    piy1 = yfinal - yfinal%div;
    piy2 = piy1+div;
    f = fopen("output.txt","r");
    while(!feof(f))
    {
        if(x>=pix1&&x<=pix2 &&x>=piy1&&y<=piy2)
        {
            if(strcmp(c,"C1")==0)
            countpi1++;
            else if(strcmp(c,"C1")==0)
            countpi2++;
        }

    }
    fclose(f);
    p1 = (float)countpi1/count1;
    p2 = (float)countpi2/count2;
    if(p1*P1>p2*P2)
        printf("point is in C1/n");
    else
        printf("point in C2");
    return 0;
}

