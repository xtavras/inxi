README for tarballs

This folder is intended to be a repository of older tarballs from svn trunk/
The Upstream Maintainer, prefers the following design:

--trunk is always by definition, the current stable live files. 
--Only one command to grab the currrent tarball, wget -Nc inxi.tar.gz 

The Tarball Maintainer, subject to approval intends to keep older tarballs here.
--not all trunk svn changes will be tarballed as sometimes there are frequent changes.

Important: the only version of inxi that is supported is the latest current svn trunk release.
No issue reports or bug reports will be accepted for anything other than current svn trunk.

The version design follows these guidelines:
Using example 1.8.14-6

The first digit(s), "1", is a major version, and almost never changes. Only a huge milestone, or, possibly, if we reach 1.9.99 and decide to then move it to 2.0.0 just to keep it clean, would cause a change. 

The second digit(s), "8", means a new real feature has been added. Not a tweaked existing feature, an actual new feature, which usually also has a new argument option letter attached. 

The third, "14", is for everything small, can cover bug fixes, tweaks to existing features to add support for something, pretty much anything where you want the end user to know that they are not up to date. 

The fourth, "6", is extra information from Tarball maintainer, when either the third digit has not changed, but there is a change or a patch comes out, and the Tarball maintainer has time to pack the change.
 
Purpose: To provide a "kind of" audit trail of most tarballs. Act as a repository of older tarballs. Users must always use the most recent tarball for support