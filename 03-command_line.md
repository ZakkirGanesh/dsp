# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. pushd /directoryname (keep track of current directory and move to new specified directory)
    2. popd (go back to directory you last pushed)
    3. touch filename (create new empty file in current directory)
    4. cp filename (copy listed files to current directory)
    5. mv oldname newname (doesn't actually move files, just renames them)
    6. code | code (pipes output on the left to the command on the right)
    7. code < code or code > code (send output from right to command on the left, vice versa)
    8. code << code or code >> code (send output from right and append to command on the left, vice versa)
    9. n* or *n (find filenames starting with "n" or ending with "n")
    10. sudo command (allows you to run command as another user)


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 'ls' lists files/folders in the home directory. 'ls -a' lists all files in the directory. 'ls -l' lists each file/folder in the directory one line at a time. 'ls -lh' lists each file/folder in the directory, line at a time, in human-readable format. 'ls -lah' lists all the files in the directory, line at a time, in human-readable format. 'ls -t' lists all files/folders in the home directory, sorted by time. 'ls -Glp' lists each file/folder in the directory, line by line, with color-coding for type, and adding "/" to directories.

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > My 5 favorite ls options are: 1) ls -R; 2) ls -l; 3) ls -a; 4) ls -G; 5) ls -p.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 'xargs' turns an arbitarily long list of parameters for an argument into more more manageable sublists of parameters. For example, if you type 'echo 1 2 3 4 5 6| xargs', you return '1 2 3 4 5 6' on 1 line, if you type 'echo 1 2 3 4 5 6| xargs -n 1', each number is listed 1 line at a time, 'echo 1 2 3 4 5 6| xargs -n 2' lists 2 numbers then goes to a new line, etc.

 

