cmake_minimum_required(VERSION 3.26)

project(phongdefo)

find_package(nanoflann CONFIG REQUIRED)
find_package(Eigen3 CONFIG REQUIRED)
find_package(HDK REQUIRED)

include_directories(
	${HDK_INCLUDE_DIR}
	)

hdk_add_plugin(SOP_TetEmbeddedDeform
	src/DeformationTracker.cpp
	src/SOP_TetEmbeddedDeform.cpp
	src/TetMesh.cpp
	)

target_link_libraries(SOP_TetEmbeddedDeform
	PRIVATE
	Eigen3::Eigen
	nanoflann::nanoflann
	)
