#include <fstream>
#include <string>
#include <iostream>

using namespace std;

int main(int argc, char *argv[]){

    // cout << argv[0] << endl; //file name
    fstream file;

    string json_name;
    json_name.assign(argv[0]).append(".json").erase(0,2);   //erases "./"
    // cout << json_name << endl;
    file.open(json_name, ios_base::out);
    //some work
    file.close();

    return 0;
}