#VisEval_Metric_Viewer

**REQUIRES (at least):** Matplotlib, Numpy, and NLTK >= 3.2.4 (see notes at the very end)

This is the first iteration of VisEval, a tool mainly written in Python, which uses a number of metrics for evaluating sentences of machine translation output against a reference file. 

The current metrics which are employed are: MT BLEU, MT NIST, NLTK BLEU, WER, TER, METEOR, BEER and Edit Distance.

All scores, various statistics, and the aligned sentences displayed in a number of HTML files, which together work like a local website that can be opened and navigated as normal in a browser (tested in Firefox, Opera, and Chrome – as well as on an Android device and an iPad).

The visual nature of the output enables the user to quickly recognise where the translation system has done well or indeed performed poorly. In addition the graphs that are generated highlight various measures and correlations that help to inform how good or bad a translation is. 

The visual format also makes it easy to spot any interesting language and scoring phenomena, and indeed highlights weaknesses and differences with automated evaluation tools.

**VisEval** requires, as parameters, 3 files, each containing the same number of sentences:

i) a source file

ii) a reference file

iii) a hypothesis file (made up of translations from a machine translation system).

The hypothesis and reference files are compared against each other for the scoring, whilst the source file is used for display purposes only. As a **minimum**, NLTK (version 3.2.4) and Numpy is required for the scoring process to run.

As well as the above there are also a number of optional flag arguments:

-h, --help show this help message and exit

###Required files:

-r REF, --ref REF the reference file to be used (required) 

-s SRC, --src SRC the source file (for display purposes only - required) 

-hp HYP, --hyp HYP the hypothesis file to be used (required)


###Optional Flags:
-g, --graphs,flag to plot and draw graphs 

-a, --advHist, show advanced histogram, (requires seaborn) 

-p, --simplePoly, show a linear line of best fit 

-nb --numberOfBins, the scores will be split up into this numberOfBins (for greater clarity and easier navigation)

-ob --orderBy, choose which metric to order by [bleu, mtbleu, mtnist, ter, wer, edit, met, beer]

-ca --colourAssist, removes some of the colours colour that can be difficult to distinguish for some users

-x --extension, an extension name or tag given to the output directory, for better separation

###Additional Metrics

By default and at its most basic level **ViSEval** will only score using: NLTK BLEU, WER, and Edit Distance.

However, additional metrics can be selected using the following flags:

-m, --meteor          include METEOR scores (requires Java)

-t, --ter             include TER scores (requires Java)

-mt, --mtEval         include MT-eval scores (includes both MT-BLEU and MT-NIST) (reuires Perl)

**NOTE**** MT-Eval requires the 'Sort-Naturally-1.03' PERL module to be installed, it is included in 

**NOTE**** VisEval/mtEval/Sort-Naturally-1.03 - Navigate to this folder and follow the README instructions.

**NOTE**** As my system has most tools installed this is the only setup error I encountered

-b, --beer            include BEER scores (requires Java)

-sz, --showZeros flag to display zero score buckets (not currently implemented, but coming soon)

By default the graphs aren’t plotted (to save time) , but using the -g flag will plot graphs and create a graphs html page as part of the building process. **(Matplotlib is required for this)**.

The -a flag only works in conjunction with -g, and when used will add a slightly prettier and more informative initial graph (histogram and boxplot). Seaborn is required for this option, which is why the simpler version is plotted by default.

The -p flag also works in conjunction with the -g flag, and if selected changes the polynomial line of best fit for a simpler linear one.

Three example files (SRC, REF, and HYP - containing 1000 sentences each) have been provided for testing purposes.
An additional HYP file has been included (nnPred.txt), which is a Neural Network translation of the src file.
It displays, in general, a slightly better set of translations than the original HYP file)

###RUNNING THE TOOL:

In order to run the tool as a test, then as a minimum the following must be completed:

Download (and unzip) OR clone the VisEval_Metric_Viewer folder...

Then do the following:

i) **cd VisEval_Metric_Viewer/VisEval_tool/VisEval**

ii) **python mainPageBuilder.py -r ref.en.txt -s src.zh.txt -hp hyp.txt**

OR (to see the Neural Network translation)

iib) **python mainPageBuilder.py -r ref.en.txt -s src.zh.txt -hp nnPred.txt**


If typed correctly, and with the minimum packages installed (Matlpotlib, NLTK (3.2.4) and Numpy), the process should run , which after a few seconds (2.8 on the test machine) should then generate the output.

The output will be saved in a vm_scores folder that will be placed one level up in the VisEval_tool folder.

The format of the saved folder will be:

The folder itself with a date stamp e.g. vm_scores_12-04-2018

Inside the vm_scores folder should be: 


###i) the main.html file, which is the entry point to the website

ii) a scorePages folder (containing all the sentence pairs and scores from the input files) 

iii) a style.css file that provides the styling for the html files 

iv) an images folder (containing all the images used in the html pages) 

v) a jQuery folder, which contains the required jquery library.

vi) a serach html file (this is used to display the search page)

vii) a dataSetStats.html file, which displays the headline scores that you often see in paper (e.g. BLEU 0.2686)

viii) an allResults.csv file, which is simply a text file showing all the rsults given in the output


Double click on the **main.html** file and it should load automatically in the default browser

You should then be able to navigate through the pages as you would a normal website

Ideally a monitor with a width of at least 1700px is best for viewing purposes

If you would like to see the graphs then experiment with the flags as outlined above

Once you are sure it works properly then feel free to point the tool to your own 3 input files and generate a more pertinent score set. If your own files are more complex than the example ones then the process may take a little longer to complete (still should be seconds rather than minutes).

Please note that currently there is just a default output save name that is time stamped per day. If you run the program more than once in a day then the earlier run will be overwritten (unless you manually rename it or use an extension tag). The option to choose your own output name will be added soon.

The per day time stamp was chosen as the original per second time stamp meant it was very easy to produce many copies of the same thing, wasting a lot of space.

Finally, please bear in mind that this is an initial version of the tool and to that end it is largely still in the testing phase. That is, the tool should work as expected, but may contain typos or similar. 

If you spot any minor issues or indeed if more serious errors are encountered then please let me know the type of error (if it isn’t caught by the software) and the circumstances under which it occurred. 

I will then try to recreate the error and fix it.

This tool was built using Python 3, but has been tested in a limited capacity using Python 2 envs (earliest is 2.4). The main issues encountered were with print statements and division of floats, which I have tried to address. 

Currently the denominators have been multiplied by 1.0 or turned into floats, rather than using ‘from future import’ statements because in some v2 environments the latter option can cause a bug.

If you have any questions or feature requests then please feel free to contact me using: dbsteele1@sheffield.ac.uk
Happy scoring :-)

###TO DO:

Add the config file option so all arguments for all metrics can be easily executed

Remove some of the prototype name that still remain

Add an argument for providing a specific output name and/or location. 

Add an argument that means the SRC file isn’t required (the user can currently type in the same file name for REF and SRC, if no proper SRC file is available, but this isn’t ideal).
 
**Note****

To upgrade to the latest NLTK, you should be able to use pip: ** pip install --upgrade nltk**

or if using conda: **conda install nltk** OR **conda update nltk**

There are other options as well: 

There is some more detail here: https://stackoverflow.com/documentation/nltk/4077/getting-started-with-nltk#t=201707072312525637183
