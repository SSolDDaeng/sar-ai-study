# B01 차시의 실행 파일 2개
add_executable(b01_hello hello.cpp)                 # 파일 하나짜리
add_executable(b01_dsp_demo main.cpp dsp.cpp
        dsp.hpp
        main.cpp)       # 파일 두 개를 따로 컴파일해 링크
