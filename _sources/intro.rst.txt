********
Prologue
********

.. sectionauthor:: Gavin Huttley

How is life encoded in nucleic acids? What is the minimum number of nucleotides required to encode a virus? Do all genetic differences between individuals contribute to phenotypic differences between them? What genetic change(s) causes humans to have unique cognitive abilities compared to our nearest great ape relatives? How many different types of microorganisms live in our gut and what role do they play in our biology? If you had :math:`\sim 10^{10}` 250bp long DNA sequences that were randomly sampled from a single Human, could you assemble that individuals genome from scratch? If you sequence DNA extracted from soil, can you identify what species the DNA comes from? If you have an assembled genome of a novel species, can you identify where the genes in the genome are?

.. sidebar:: What's the difference between using Python_ versus using R_?

    Both languages provide very sophisticated capabilities for scientists, hence they are the dominant languages employed in Data Science. Both of these languages are also `Open Source <https://en.wikipedia.org/wiki/Open_source>`_ languages, developed by a community of volunteers [3]_.
    
    The major difference between Python_ and R_ comes in how they are typically used [4]_. Many of the concepts you will learn in the Python_ topic -- conditionals, iteration, functions -- are not directly coded by most users of R_. They are implicitly being used, but are "hidden" from users.
    
    The way you will learn Python_ is as a more "conventional" programming approach.

We do not know the answer to many of these questions. Despite that, and despite the fact that some of them are strictly concerned with biological phenomena, I am confident that they all require computers to attain a solution. I will go even further and claim that any question in the biological sciences we can come up with will require the use of computers to tackle it. Based on this, I think it is reasonable to make the general claim that biologists have a near absolute reliance on computers for undertaking their research [1]_. But we can make that statement more specific: Biologists have a near absolute reliance on **software** to undertake their research [2]_.

Just about every part of a biology wet-lab has some type of digital device, from pipette's and scales to centrifuges. From confocal microscopes to scanning tunnelling electron microscopes. The more transformed data becomes from the natural system, the greater the involvement of software (and our reliance on it) to control those devices. But science is an enterprise whose objective is much more than simply the accumulation of data. Similarly, software can be much more than instructions for controlling the capture of data.

Science is about producing general models of how the natural world works. Good scientific models are powerful because they allow us to make predictions about what we will observe in circumstances that have not yet been encountered. Computer programs are one way in which we represent those models. They provide us with the means to evaluate, on a large scale, how well our model matches actual data. In other words, software is integral to scientific practice.

.. [1] I suspect this holds true for all the sciences.
.. [2] Software is just another word for computer program. The computer is just a piece of hardware but the software is the specific set of instructions that dictate what that hardware does.

The above is a big picture view of the role of software in science, but where does this course fit in? I can say with absolute certainty that we will not be answering most of the questions raised above (Doh!). What *you* will be doing is acquiring the skills necessary to understand what the analyses described above are, how to perform them and whether *you* should believe the results. *You* will develop the skills to write custom software whose output you can trust. In your future career, that software may be as simple as handling data formats, or completely novel models of biological systems. In all cases, your software will be key to solving the scientific questions that you find interesting.

At this stage, I'm sure you have many questions. Like, *What is "bioinformatics"?* *I've heard the phrase "Data Science", is that what bioinformatics is?*

.. |Python| replace:: *Python*
.. |R| replace:: *R*

.. [3] I could write a very extensive essay on how open source software has, and continues to be, critical to science. Instead I have used the quote from Paul Romer to illuminate the fact that true scientific reproducibility requires transparency. By definition, open source software satisfies this condition while proprietary software does not.

.. [4] Ok, Ok, I get it. This is a gross oversimplification of the differences between the languages.

:index:`Data Science` is the joint application of algorithm development and statistical modelling to extracting information from what is referred to as "big data". Bioinformatics, also referred to as computational biology, certainly fits within this rather loose definition. In essence, Bioinformatics is the union of algorithms and statistics focussed on extracting information from big biological data sets to advance knowledge of biological systems.

.. seriously, need to acknowledge that languages are different

.. todo:: include description of computational thinking, how that part is not about programming, per se, but shares similarities. Using abstraction; Decomposition; Separation of concerns;

.. todo:: add commentary on mechanics of programming being just part of the skill set, it's really the ability to transform a biological research question into a form that can be addressed using algorithm

*What will I get out of this course?* An understanding of how computer programs work. Improvements in your logical reasoning. An understanding of how to take advantage of computing to advance your own scientific interests. An appreciation of the pitfalls of software! All of this adds up to a superpower that will accelerate your work [5]_.

.. [5] Sorry, it's bring your own cape.

