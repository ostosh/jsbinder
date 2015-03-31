#
# Copyright (C) 2015 Opersys inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
    "targets": [
        {
            "target_name": "jsbinder",
            "include_dirs": [
                "external/include",
            ],
            "cflags": [
                "-include AndroidConfig.h"
            ],
            "defines": [
                "ANDROID_SMP=0"
            ],
            "sources": [
                "external/binder/Binder.cpp",
                "external/binder/BpBinder.cpp",
                "external/binder/IInterface.cpp",
                "external/binder/IMemory.cpp",
                "external/binder/IPCThreadState.cpp",
                "external/binder/IPermissionController.cpp",
                "external/binder/IServiceManager.cpp",
                "external/binder/MemoryBase.cpp",
                "external/binder/MemoryDealer.cpp",
                "external/binder/MemoryHeapBase.cpp",
                "external/binder/MemoryHeapPmem.cpp",
                "external/binder/Parcel.cpp",
                "external/binder/Permission.cpp",
                "external/binder/ProcessState.cpp",
                "external/binder/Static.cpp",

                "external/utils/BufferedTextOutput.cpp",
                "external/utils/CallStack.cpp",
                "external/utils/Debug.cpp",
                "external/utils/FileMap.cpp",
                "external/utils/Flattenable.cpp",
                "external/utils/Looper.cpp",
                "external/utils/misc.cpp",
                "external/utils/ObbFile.cpp",
                "external/utils/PackageRedirectionMap.cpp",
                "external/utils/Pool.cpp",
                "external/utils/RefBase.cpp",
                "external/utils/ResourceTypes.cpp",
                "external/utils/SharedBuffer.cpp",
                "external/utils/Static.cpp",
                "external/utils/StopWatch.cpp",
                "external/utils/String16.cpp",
                "external/utils/String8.cpp",
                "external/utils/StringArray.cpp",
                "external/utils/SystemClock.cpp",
                "external/utils/tests",
                "external/utils/TextOutput.cpp",
                "external/utils/Threads.cpp",
                "external/utils/Timers.cpp",
                "external/utils/VectorImpl.cpp",

                "external/libcutils/buffer.c",
                "external/libcutils/uio.c",
                "external/libcutils/socket_local_client.c",
                "external/libcutils/socket_loopback_server.c",
                "external/libcutils/native_handle.c",
                "external/libcutils/socket_inaddr_any_server.c",
                "external/libcutils/properties.c",
                "external/libcutils/load_file.c",
                "external/libcutils/dir_hash.c",
                "external/libcutils/ashmem-host.c",
                "external/libcutils/record_stream.c",
                "external/libcutils/tztime.c",
                "external/libcutils/open_memstream.c",
                "external/libcutils/cpu_info.c",
                "external/libcutils/strdup16to8.c",
                "external/libcutils/socket_local_server.c",
                "external/libcutils/threads.c",
                "external/libcutils/dlmalloc_stubs.c",
                "external/libcutils/iosched_policy.c",
                "external/libcutils/sched_policy.c",
                "external/libcutils/config_utils.c",
                "external/libcutils/socket_network_client.c",
                "external/libcutils/abort_socket.c",
                "external/libcutils/strdup8to16.c",
                "external/libcutils/array.c",
                "external/libcutils/process_name.c",
                "external/libcutils/zygote.c",
                "external/libcutils/mq.c",
                "external/libcutils/socket_loopback_client.c",
                "external/libcutils/atomic.c",
                "external/libcutils/selector.c",
                "external/libcutils/hashmap.c",

                "external/liblog/event_tag_map.c",
                "external/liblog/fake_log_device.c",
                "external/liblog/logd_write.c",
                "external/liblog/logprint.c",

                "lib/jsbinder.cpp"
            ]
        }
    ]
}
