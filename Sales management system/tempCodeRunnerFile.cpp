#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
int main()
{
char buf[20][20],infile[20],outfile[20],buf1[20];
char line[200];
int i,j,indx,x,y,ch;
fstream file,file1;
cout<<"Enter your choice\n1->file I/O\n2->standard I/O";
cin>>ch;
switch(ch)
{
case 1:{ cout<<"Enter the input file:"<<flush;
cin>>infile;
cout<<"Enter the output file:"<<flush;
cin>>outfile;
file.open(infile,ios::in);
file.unsetf(ios::skipws);
file1.open(outfile,ios::out);
while(1)
{
file.getline(line,200,'\n');
if(file.fail())
break;
else
{
} }
file.close();
for(i=strlen(line);i>=0;i--)
file1<<line[i];
file1<<"\n";
file1.close();
}
break;
case 2:{ cout<<"Enter the sequence of names or '0' to exit";
indx=0;
while(1)
{
cin>>buf[indx];
if(strcmp(buf[indx],"0")==0) break;
indx++;
}
for(i=0;i<indx;i++)
{
for(j=strlen(buf[i]);j>=0;j--)
cout<<buf[i][j];
cout<<endl;
}
}
break;
}
return 0;
}
