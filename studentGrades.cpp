#include<iostream>
#include<cstdio>
#include<cstring>
#include<bits/stdc++.h>
#include<fstream>
using namespace std;

int main(){
	string rollNum;
	string word;
	ifstream infile;
	int marks;
	infile.open("marksList.txt");
	map<string, int>student_marks;
	while (infile){
		infile>>rollNum;
		infile>>marks;
		student_marks[rollNum] = marks;
	}
	int itr=0;
	for (itr = student_marks.begin(); itr != student_marks.end(); ++itr) { 
        cout << '\t' << itr->first 
             << '\t' << itr->second << '\n'; 
    } 
	return 0;
}

