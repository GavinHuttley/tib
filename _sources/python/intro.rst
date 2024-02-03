Introduction to programming using Python
========================================

If you have ever used Instagram, or Dropbox or YouTube, then you have used an application written largely in Python. It's `an extremely popular`_ general purpose programming language. For a variety of reasons, it has become even more popular in the sciences -- it was integral to at least `one Nobel Prize`_.

It's worth emphasising a few things up front. We all use software every day. How we interact with that software is exclusively via a graphical user interface (GUI). In contrast, most bioinformatics software does not have a GUI.

Data analysis software which does have a GUI, represents a barrier to reproducibility. That's because the steps used to perform an analysis are typically not recorded, so the analysis cannot be "replayed".

In this course, we will be developing and using non-GUI software. We will be doing our work in Jupyter notebooks. These provide access to programming environments within a web browser.

.. note:: Text that has ``this`` font style represents a statement in Python.

Using these notes
-----------------

The best way for you to learn a programming language is by "doing". Every place where you see code segments in the notes, you should try it yourself. This act of replicating the code is educational because of the inevitable errors you will make which lead you start exercising your skills in debugging!

What is a program?
------------------

A program is a series of instructions specifying how to do a computation that is written in a "programming language". Programming languages have rules about program structure, called *Syntax*. This can be very much like what you already understand from mathematics, e.g.

✅ (8+2)

❌ 8+2)

How a computer works
--------------------

In the truly simplest sense! The main components defining execution of a program are *inputs*, *process* and *outputs*. The "program" is the "process" part. A program is defined by *source code*, instructions written in a text file in a specific language dialect.

.. digraph:: foo

    rankdir="LR"
    a [shape="note" label="Source code"]
    b [shape="square" label="Interpreter"]
    c [shape="box3d" label="Output"]
    a -> b -> c;

.. note, I can use images for nodes, e.g. imgnode[image="apple-touch-icon.png", label=""];

There are of course other elements that define a computer. For instance, storage. A *hard drive* is persistent storage. This is where your documents and programs live. These survive turning of your computer. Programs, documents, etc.., are loaded (or read) from the hard drive into memory. *Memory* or *RAM* (random access memory) is volatile storage, meaning if you turn off your computer, what was in RAM is lost.

Basic program elements
----------------------

All programming languages specify "keywords". These are the logical units from which a program is constructed.

**input**
    "Data" provided to a program, e.g. a file, or keyboard input from a user.

**output**
    The result of applying a program to data.

**maths**
    operations that you know and love! These involve standard operators, e.g. ``+``, ``-``, ``*`` (multiplication), ``/`` (division), ``**`` (power).

**conditional execution**
    This is a type of "flow control" statement. The conventional keywords are ``if``, ``else`` and (in Python) ``elif``.

**repetition or looping**
    A type of control statement specifying conditions under which a task is to be repeated. Conventional keywords are ``for``, ``while``.

💣 → Errors → Debugging
-----------------------

Dealing with errors is a standard, inevitable, part of programming. The process of fixing errors is termed debugging. You can reduce the number of errors you make in writing a program by breaking the algorithm into small pieces, writing one piece, checking it works and then move onto the next piece.

.. margin:: Minimise time fixing errors

    Even if you could write an entire complex algorithm in one go, doing so is a bad idea.

    A multitude of procedures are employed improve the reliability of software, some of which are quite elaborate. But one thing all such approaches have in common is to **write a small amount of code and then run it**, fixing any errors each time. If the program stops running, you know the responsible code is only what you just entered.

There are different classes of errors:

- Syntax → code is not valid Python
- Runtime → something bad happened during run
- Logic → code produces incorrect answers

These errors can cause a program to stop executing. If that happens, Python produces a *traceback* -- a display of the type of error, where (what line) it occurred at and the full series of references in the program that triggered the error. These tracebacks are extremely informative.

Python has a very extensive set of error types which fall into the Runtime error group. This variety is useful as the type of error provides important clues as to why the program failed.

The most insidious error type are the Logic errors. In this case, the program can complete and produce output. We deduce there's a logical error because the output is wrong! This is where writing tests of your software becomes crucial.

.. _`an extremely popular`: http://pypl.github.io/PYPL.html
.. _`one Nobel Prize`: https://qz.com/1417145/economics-nobel-laureate-paul-romer-is-a-python-programming-convert/
.. _`open access text book on Python`: http://greenteapress.com/wp/think-python-2e/
.. _`free Python IDE`: https://wingware.com/downloads/wingide-personal
