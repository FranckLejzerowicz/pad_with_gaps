# pad_with_gaps

This little script simply adds gaps (hyphens) as the end of each sequence provided in a fasta file so that the number of characters in sequence is the same (that of the longest input sequence).

This is useful for running programs such as [Oligotyping](http://merenlab.org/software/oligotyping/) or for loading the fasta file in an alignment parser such as [AlignIO](http://biopython.org/DIST/docs/api/Bio.AlignIO-module.html) for [Biopython](http://biopython.org/).

## Usage
```
python  pad_with_gaps.py [-h] -i I -o O
```

### Optional arguments
```
  -h, --help  show help message and exit
  -i I        Input fasta file (required)
  -o O        Output fasta file (required)
```

### Example

##### Input fasta file

```
>Seq1
ATATCGGTAGCTGATGTGCTAGTGTGC
>Seq2
ATATCGGTAGCTGATGTGC
>Seq3
ATATCGGTAGCTGATGTGCTAGC
```

##### Output fasta file

```
>Seq1
ATATCGGTAGCTGATGTGCTAGTGTGC
>Seq2
ATATCGGTAGCTGATGTGC--------
>Seq3
ATATCGGTAGCTGATGTGCTAGC----
```


### Requirements

* python2.7
* Biopython
