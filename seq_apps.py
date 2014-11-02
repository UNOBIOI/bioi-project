from Bio.Seq import Seq
from Bio.Blast import NCBIWWW
from Bio import SeqIO

#ask for user's sequence
my_seq = raw_input("\n\nEnter nucleotide sequence: ")
my_seq = my_seq.upper()

#create file to write the sequence as a fasta file. 
f = open("user_input.fasta","w")
f.write(">user's input\n" + my_seq)
f.close()

#format the inputed sequence into biopythons preference
my_seq = Seq(my_seq)

print '\n\nThe sequence is %i bases long' % (len(my_seq))
print 'The reverse complement is %s' % my_seq.reverse_complement()
print 'The protein translation is %s\n\n' % my_seq.translate()

#counting the composition
a_comp = my_seq.count("A")
g_comp = my_seq.count("G")
c_comp = my_seq.count("C")
t_comp = my_seq.count("T")

print "A composition is: %i" % a_comp
print "G composition is: %i" % g_comp
print "C oomposition is: %i" % c_comp
print "T composition is: %i" % t_comp


