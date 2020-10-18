# JS Binder Library

This module has been updated to work on later versions of Android but unfortunately this makes the process of building it much more difficult. Check the ./build_all.sh script if you want to know how it works. 

Check in the releases section of this site to see prebuilt packages that can be copied in node_modules.

The Brave Individuals that may want to build and use this module in their own projects should do the following.

Get Node.js for Android sources from:
https://github.com/opersys/node

In the node-android directory:
source ./android-configure

In the jsbinder directory:
node-gyp --arch=arm --nodedir=node-android directory

This should give you the .so needed for Android. The proper use of this module within another project is left as an exercise to the reader while we figure out a more friendly way to make Android-based Node.js project.
