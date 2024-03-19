#include <windows.h>
#include <cstdio>
#include <iostream>
#include <string>

int __stdcall GenSerial__10001020(LPCSTR Name, LPCSTR Company, LPSTR String, int a4)
{
    unsigned __int8 v4; // bl
    int v5; // edi
    int v6; // ebp
    int v7; // eax
    int v8; // esi
    CHAR v9; // dl
    CHAR v10; // cl
    unsigned __int8 v11; // dl
    unsigned __int8 v13; // [esp+11h] [ebp-107h]
    unsigned __int8 v14; // [esp+12h] [ebp-106h]
    unsigned __int8 v15; // [esp+13h] [ebp-105h]
    int v16; // [esp+14h] [ebp-104h]
    CHAR StringBuffer[256]; // [esp+18h] [ebp-100h] BYREF

    v13 = 0;
    v14 = 0x20;
    v4 = 8;
    v15 = 0x27;
    v5 = 2;
    v6 = 4;
    if (!Name || !Company || !String || lstrlenA(Name) > 0x20 || lstrlenA(Company) > 0x40 || a4 < 0x10)
    {
        return 0;
    }

    wsprintfA(StringBuffer, "%s%s", Name, Company);
    v7 = lstrlenA(StringBuffer);
    v8 = 0;
    v16 = v7;
    if (v7 > 0)
    {
        while (1)
        {
            if (v5 >= v7)
            {
                v5 = 0;
            }

            if (v6 < 0)
            {
                v6 = v7 - 1;
            }

            v9 = StringBuffer[v8];
            v13 += v9;
            v14 += v9 * StringBuffer[v5];
            v10 = StringBuffer[v6];
            v4 -= v10 * StringBuffer[v8 + 1];
            v11 = (StringBuffer[v5++] & (v9 | v10)) + v15;
            --v6;
            ++v8;
            v15 = v11;
            if (v8 >= v16)
            {
                break;
            }

            v7 = v16;
        }
    }

    wsprintfA(String, "%3.3d-%3.3d-%3.3d-%3.3d", v13, v4, v15, v14);
    return 1;
}

int main() {
    CHAR Serial[256];
    std::string name;
    std::string company;

    std::cout << "Enter your name: ";
    std::getline(std::cin, name); // Đọc dòng văn bản từ bàn phím

    std::cout << "Enter your company: ";
    std::getline(std::cin, company); // Đọc dòng văn bản từ bàn phím

    // Chuyển đổi từ std::string sang LPCSTR
    LPCSTR namePtr = name.c_str();
    LPCSTR companyPtr = company.c_str();
    int a4 = 0x100;

    if (GenSerial__10001020(namePtr, companyPtr, Serial, a4)) {
        printf("Serial: %s\n", Serial);
    }
    else {
        printf("Error generating serial.\n");
    }

    return 0;
}
