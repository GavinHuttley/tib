********
Prologue
********

.. sectionauthor:: Gavin Huttley

.. todo:: add commentary on mechanics of programming being just part of the skill set, it's really the ability to transform a biological research question into a form that can be addressed using algorithm

.. epigraph::

    “The more I learn about proprietary software, the more I worry that objective truth might perish from the earth”
    
    --- Professor Paul Romer, Awarded the 2018 Nobel Prize in Economics, and Python Programmer.

A striking scientific trend in the last few years is demonstration of a `replication crisis`_. In short, this is the result of systematic examination of the extent to which published scientific studies are reproducible. It is termed a "crisis" because it turns out there is a significant fraction of studies that could not be reproduced. So what does this have to do with bioinformatics? Read on.

At this stage, I'm sure you have many questions. Like, *What is "bioinformatics"?* *I've heard the phrase "Data Science", is that what bioinformatics is?* *Why are you teaching Python for part of the course and R for the rest?*

Let's go backwards. We teach Python and R because these are the languages that we use in our own research. We use these languages because they have capabilities that allow us to leverage very sophisticated capabilities for our science. It also turns out that these two languages are the dominant languages employed in Data Science.

.. sidebar:: What's the difference between Python and R?

    The major difference between Python and R comes in how they are typically used. Many of the concepts you will learn in the Python topic -- conditionals, iteration, functions -- are not directly coded by most users of R. They are implicitly being used, but are "hidden" from users.
    
    The way you will learn Python is as a more "conventional" programming approach.

.. todo:: the benefits, a different way of seeing, logical improvements in work, super power

:index:`Data Science` is the joint application of algorithm development and statistical modelling to extracting information from what is referred to as "big data". Bioinformatics, also referred to as computational biology, certainly fits within this rather loose definition of data science. In essence, Bioinformatics is the union of algorithms and statistics focussed on extracting information from big biological data sets to advance knowledge of biological systems.

.. seriously, need to acknowledge that languages are different

We can ask, "What is the role of computing in science?" First, I hope you accept that science is about producing general models of how the natural world works. Good scientific models are powerful because they allow us to make predictions about what we will observe in circumstances that we may never have encountered before. Computer programs are one way in which we represent those models. They provide us with the means to evaluate, on a large scale, how well our model matches actual data. In other words, computing is at the very centre of scientific practice.

*What will I get out of this course?* An understanding of how computer programs work. Improvements in your logical reasoning. An understanding of how to take advantage of computing to advance your own scientific interests. An appreciation of the pitfalls of software!

Back to the replication crisis. When given the same input, computer programs are, by design, intended to produce the same output. Given computing is a central part of science, its usage needs to be done with replication in mind.

It is my goal that after this course your awareness on how to write code and validate its correctness makes you part of the solution to the replication crisis.

.. _`replication crisis`: https://en.wikipedia.org/wiki/Replication_crisis

.. todo:: add section on how to contribute, "Edit on GitHub" etc..
