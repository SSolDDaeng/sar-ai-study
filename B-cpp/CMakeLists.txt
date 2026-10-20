# B-cpp 전체를 하나의 CMake 프로젝트로 묶는 최상위 파일
cmake_minimum_required(VERSION 3.22)      # Ubuntu 22.04 기본 cmake(3.22)로도 동작
project(sar_ai_study_cpp LANGUAGES CXX)   # 프로젝트 이름, C++만 씀

set(CMAKE_CXX_STANDARD 20)                # -std=c++20
set(CMAKE_CXX_STANDARD_REQUIRED ON)       # C++20을 못 하면 오류로 멈춤
set(CMAKE_CXX_EXTENSIONS OFF)             # gnu++20 대신 표준 c++20
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)     # 편집기용 compile_commands.json 생성

add_compile_options(-Wall -Wextra -Wpedantic)  # 경고를 넉넉히 켬

add_subdirectory(B01)                     # 차시가 늘면 여기에 한 줄씩 추가
