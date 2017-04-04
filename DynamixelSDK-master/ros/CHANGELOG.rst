^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package dynamixel_sdk
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3.4.1 (2016-08-22)
-----------
* added ROS package folder for ROS users
* modified original header files for ROS package

3.4.0 (2016-08-12)
-----------
* first public release for Kinetic
* added package information for wrapping version for ROS
* added ROS catkin package files.
* linux build file for SBC
* License marks for example codes
* Resource Files comments Korean -> English
* Update Makefile
* Update Makefile
* comments modified & aligned
* Release folders in c++ example removed & dxl_monitor.cpp Capital function name modified as ROS c++ code style & included file paths of packet/port handler in dynamixel_sdk.h removed and added parent header file
* Update dxl_monitor.cpp
* file opened
* folder name modification error solved
* License specified
* Code Style modified into ROS C++ coding style
  Function & File Names changed into underscored
* Group Bulk/Sync class ClearParam() function changed.
* dll file name changed
* dll file name changed
* Comment modified
* [Protocol1PacketHandler]
  RxPacket packet length re-calculate bug fixed.
* [Protocol2PacketHandler]
  RxPacket packet length re-calculate bug fixed.
* Makefile updated
  Source reorganization
* Windows version updated
  Makefile modified
  Source reorganization
* GroupBulkRead : GetData function bug fixed.
* [GroupBulkRead / GroupSyncRead]
  added IsAvailable() function
  modified GetData() function
* GetData() function changed.
* reducing the count of calling MakeParam function
* added rxpacket error check
* ReadTxRx function modified. (to use TxRxPacket function)
* DXL Monitor program arguments added.
* if the last bulk_read / sync_read result is failure -> GetData return false
* communication result & rx packet error print function modified.
* first release
* Contributors: Leon, ROBOTIS, ROBOTIS-zerom, leon, pyo, sadtale
