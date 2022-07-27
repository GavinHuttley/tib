.. index::
    pair: string; types

.. _strings:

Dealing with strings
====================

Text is the dominant way in which bioinformatics data is stored and shared. So any bioinformatician needs to become expert in manipulating text data.

The most common tasks concern:

- Transforming lines in a file into data types that can be processed
- Transforming python objects into text so it can be written to a file

All such text manipulation involves the string data type, so becoming deeply familiar with what strings are and how to interrogate and manipulate them is crucial.

Creating a string type from a non-string type
---------------------------------------------

All objects in python can be turned into a string using the ``str()`` function.

.. jupyter-execute::

    num = 42
    num_as_str = str(num)
    print(type(num_as_str), num_as_str)

Even complex objects, which I demonstrate using a list.

.. jupyter-execute::

    data = ["text", 42, 3.14]
    data_as_str = str(data)
    data_as_str

Being able to convert complex objects into strings is useful for display to screen since it gives you exact insight into the state of an object during program execution. It's less useful as precursor for storage because there is no universally simple (and secure) operation for reconstructing the original objects. This latter issue is a case of "data serialisation" and is beyond the scope of these notes [1]_.

.. [1] The native serialisation approach for Python is called `pickling <https://docs.python.org/3/library/pickle.html>`_. This approach has many problems. A popular alternative is `json <https://docs.python.org/3/library/json.html>`_.

Defining strings
----------------

Defining a string can be done using balanced quote marks. You can use either single (``'``), or double (``"``) quotes. For instance

.. jupyter-execute::

    single = 'text'
    single

and

.. jupyter-execute::

    double = "text"
    double

are both valid and equal.

.. jupyter-execute::

    single == double

The convention is to use double quotes.

An empty string is defined by balanced quotes with nothing between them.

.. jupyter-execute::

    empty = ""

How to include a quote character in a string
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since we define a string using quotes, including a quote character can be solved in two ways. By "escaping" (see :ref:`escaping_chars`) the quotes with a preceding backslash (``\``).

.. jupyter-execute::

    text = "escaping \"quotes\""
    print(text)

Or, defining the string with the other type of quote. In this example, the string is defined using single quotes so we can safely include double quote characters in the string. This approach is preferred since it's more readable.

.. jupyter-execute::

    text = 'escaping "quotes"'
    print(text)

.. index::
    pair: literal; string

Literal strings
---------------

This is a special case in which the strings can include line breaks and other formatting. These are created by triple-quoting. For instance

.. jupyter-execute::

    multi_line = """We can have multiple lines of content.

    And blank lines etc..
    """
    print(multi_line)

The actual formatting is revealed by using the representation of the object [2]_.

.. [2] In an interactive interpreter, you do not need to do anything special to see this, other than simply having a statement that consists of only the variable name itself. In a python script, however, you would need to print the result of calling ``repr()``, i.e. ``print(repr(multi_line))``

.. jupyter-execute::

    multi_line

Literal strings are most often used for writing documentation strings (or docstrings) on functions and methods.

.. index::
    pair: tab; string
    pair: new line; string
    pair: space; string
    pair: white space; string

Special characters in strings – tabs, new lines, spaces
-------------------------------------------------------

White space exists in files in part to make it easier for humans to understand the contents. (Reading this text if there were no spaces between the words would be a massive cognitive strain.) It also exists in files to make it easier to separate different types of data. So it is crucial to know what white space is (beyond it's central role in the Python language itself). I'm showing the most common below.

.. jupyter-execute::

    using_space = "separate words"
    print(using_space)

.. jupyter-execute::

    using_tab = "separate\twords"
    print(using_tab)

.. jupyter-execute::

    using_newline = "separate\nlines"
    print(using_newline)

Finding out things about a string
---------------------------------

We often want to know whether a string contains a particular character or substring [3]_. There are specific string methods and more general Python approaches to discovering this.

.. [3] a substring is just a smaller string than what you currently have. For example, `"b"` is a substring of ``"ab"``.

Using standard Python operators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's look at the general Python approach first. We can compare strings in a number of ways. We can ask whether they have the same value.

.. jupyter-execute::

    i = "ab"
    j = "b"
    i == j

We can ask whether a substring is part of a string using the ``in`` operator.

.. jupyter-execute::

    j in i

In this second case, there is no information about where the substring is located only that there is a "match".

Using string methods
^^^^^^^^^^^^^^^^^^^^

If you're not sure what a method is, read :ref:`methods`. Briefly, if we want to establish whether some text data has a particular property we first need to be able to reference the data by the name of the variable storing it. This variable is called an "instance" of type ``str``. In object-oriented languages like python, we then use *a method on that instance* to evaluate the property of interest.

Returning to the task of finding substrings, we can establish whether a string contains a substring using the ``find()`` method. In this case, an integer is returned.

.. jupyter-execute::

    index = i.find(j)
    type(index), index

In this case, the value tells you whether the substring exists (``index >= 0``) and where, in the string, the first instance occurs. There are other search related methods too [4]_.

.. [4] Another, extremely powerful, approach to querying strings in a more general way is achieved by using regular expressions (also referred to as regexes). Again, unfortunately, these are beyond the scope of this course. That said, you should definitely `read about them <https://docs.python.org/3/howto/regex.html>`_.

.. note:: The general pattern in using a method is you first specify the object and then the method of interest like so ``<instance>.<method name>()``.

Useful string descriptor methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Other common string processing tasks concern checking the beginning of a string, or the end of a string. The former is commonly encountered for processing file formats where lines start with specific characters. The latter commonly encountered when processing filenames.

.. jupyter-execute::

    path = "data/chrom1.fa"
    is_data = path.startswith("data")
    is_data

Transforming strings
--------------------

One common string transformation operation involves removing specific characters. Here it's useful to utilise positional information. For instance, if you're reading lines from a text file you know that the line will end with a trailing new line character (depending on your operating system). In this instance, the ``strip()`` method is what you want. The steps to doing this are:

1. Have the variable of interest
2. Call the ``strip()`` method
3. Assign the result of the call to a variable.

In this example, I'm defining a ``line`` variable with leading and trailing white space and some internal white space of different types. To remove leading/trailing using strip.

.. jupyter-execute::

    line = "  ORF1ab\t himalayan  palm civet\n"
    line

.. jupyter-execute::

    trimmed = line.strip()
    trimmed

Another approach to removing characters is to use the ``replace()`` method. Removing the new line character is easy, since it is unique. We replace characters by specifying what we want to replace and what we wish to replace it with. In this case, we wish to remove the ``"\n"`` and replace it with nothing so we specify an empty string as the second argument.

.. jupyter-execute::

    trimmed_via_replace = line.replace("\n", "")
    trimmed_via_replace

That doesn't address the leading spaces problem. We could do so by ``line.replace(". ", "")``, but that has an unfortunate side-effect.

.. jupyter-execute::

    trimmed_via_replace = trimmed_via_replace.replace("  ", "")
    trimmed_via_replace

We have concatenated two words together because there was a double space between them too. So ``strip()`` is better for handling the start/end of strings.

Another key string transformation is to split a string into pieces. Working with ``trimmed``, if we split at the tab character (``"\t"``) we get a list of strings back.

.. jupyter-execute::

    data = trimmed.split("\t")
    data

If we then want to clean up the items in ``data``, removing their leading trailing spaces, we need to call ``strip()`` on each item. This is solved by doing a loop.

.. jupyter-execute::

    data = [item.strip() for item in data]
    data

In doing that we can see there's still two spaces in one item. We will address that at the end.

Preparing data for writing to file
----------------------------------

In order to do this, we often need to concatenate items into being a single string. The most common so called "delimited" file format is csv (which stands for comma separated). So we will now convert ``data`` into a single string with the items separated by a comma.

In this case, our data instance is a list and its items are all strings. Transforming these into a single string requires defining the string you want to join them with and using the ``join()`` method on **that** instance.

.. jupyter-execute::

    csv_line = ",".join(data)
    csv_line

This output highlights the fact that one of the items has an unwanted double space. How can ensure that we have a csv delimited file where all items are separated by a single space and have no leading or trailing white space?

We do that by combining the above. We start by doing it the long-handed, but explicit, way -- using a for loop -- building the algorithm up in increasingly longer pieces.

We start again with the tab-split.

.. jupyter-execute::

    data = trimmed.split("\t")

We then loop over the items in ``data``, and apply strip and then split. Why in that order? because ``strip()`` works with the ends of the string and returns another string while ``split()`` affects the entire string.

.. jupyter-execute::

    cleaned = []
    for item in data:
        item = item.split()
        print(item)

That output shows, the first time through the loop, we get back a list with a single member. The Second time through the loop, we get back a list with 3 members. What we want is to join the words with a single space. We know from above what ``join()`` will do on a list with multiple members (puts the character in between them), but what will it do to a list with one member? Let's experiment!

.. jupyter-execute::

    one = ["one"]
    " ".join(one)

That experiment shows the method will just return the single string member. Awesome! So let's transform list ``item`` in our ``for`` loop into a string using this join.

.. jupyter-execute::

    cleaned = []
    for item in data:
        item = item.split()
        item = " ".join(item)
        print(item)

Well that works, so now let's just add it to the ``cleaned`` list variable.


.. jupyter-execute::

    cleaned = []
    for item in data:
        item = item.split()
        item = " ".join(item)
        cleaned.append(item)
    
    cleaned

Getting excited now! Let's finish off this production of a cleaned csv delimited line.

.. jupyter-execute::

    cleaned = []
    for item in data:
        item = item.split()
        item = " ".join(item)
        cleaned.append(item)
    
    cleaned = ",".join(cleaned)
    cleaned

Not done yet...
^^^^^^^^^^^^^^^

We can clean this code up quite a bit. First, we can combine the first two lines of the loop into a single statement. Because the ``split()`` method returns an instance that's compatible with the required input of the ``join()`` method, we can combine these into a single statement without needing to define an intermediate variable.

.. jupyter-execute::

    cleaned = []
    for item in data:
        item = " ".join(item.split())
        cleaned.append(item)
    
    cleaned = ",".join(cleaned)
    cleaned

This does exactly the same thing as before since – just like in mathematics – expressions are evaluated from the inner most parentheses first (i.e. ``item.split()`` is called first, then ``" ".join()``).

We can go further since the result of  ``" ".join()`` produces output compatible with the required input of ``append()``.

.. jupyter-execute::

    cleaned = []
    for item in data:
        cleaned.append(" ".join(item.split()))
    
    cleaned = ",".join(cleaned)
    cleaned

And even further

.. jupyter-execute::

    cleaned = [" ".join(item.split()) for item in data]
    cleaned = ",".join(cleaned)
    cleaned

and further

.. jupyter-execute::

    cleaned = ",".join([" ".join(item.split()) for item in data])
    cleaned

Just because you can doesn't mean you should!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hopefully, that's not an unfamiliar realisation. The difference between the long-winded way and the much more compact expression is, at least, a loss of some clarity. The more compact expression is somewhat harder to understand and definitely harder to debug should anything go wrong.

My advice is to be more verbose as you learn to program and gradually increase the compactness of your code as these patterns become more familiar.

But wait, it's still not ready to write to a file!
--------------------------------------------------

Good catch! Unless you really want to have all your data on a single line, you should end the line with a line feed character. This can be done with the following addition

.. jupyter-execute::

    out = cleaned + "\n"

and then this can be safely written into a file onto its own line and thus readily recovered at a later date.

Other really useful methods on string objects
---------------------------------------------

.. csv-table:: Useful string methods
    :header: Method name, Method does

    ``count()``, Counting characters in the string.
    ``encode()``, Converting to a different character sets (e.g. to bytes).
    ``startswith()``, Whether string starts with a substring.
    ``endswith()``, Whether string ends with a substring.
    ``find()``, Find the index of substring.
    ``index()``, Like find but raises an exception if not present.
    ``replace()``, Replace substring.
    ``splitlines()``, Splits the string at new line characters.
    ``lower()``, Convert the string to all lower case.
    ``upper()``, Convert the string to all upper case.

These are all accessed using the ``<instance variable>.<method name>()`` approach.

Exercises
=========

.. jupyter-execute::

    text = "        Use this sample text\n\tfor the following\n        exercises.\n  "
    print(text)

Using ``text``:

#. Remove leading / trailing white-space.

#. Replace each tab character with 8 spaces.

#. Split ``text`` into a list of the separate lines.

#. Using the result of the last step, concatenate using a single space character.

#. Write two successive python statements that transform ``text`` so that there are only single spaces between words and there are no line-breaks?

    The expected output is.

    .. jupyter-execute::
        :hide-code:

        print(repr(" ".join(text.split())))

