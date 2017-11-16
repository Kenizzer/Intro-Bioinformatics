#Generate file with only varients above qual score 40
	$ cat sim_reads_1M_variants.vcf | awk -F '\t' '/^#/ {print;next;} { if(($6)>= 40) print;}'

# Count number of entries to start
	$ grep -v -E "^#" sim_reads_1M_variants.vcf | wc -l

##Result: 4264

# Count number of entries after filtering
	$ cat sim_reads_1M_variants.vcf| awk -F '\t' '/^#/ {print;next;} { if(($6)>= 40) print;}' | grep -v -E "^#" | wc -l

##Result: 2289

#Check for the list of quality score of records in VCF file
#will generate a reverse list of colmun 6 of the file
	$ cat sim_reads_1M_variants.vcf| awk -F '\t' '/^#/ {print;next;} { if(($6)>= 40) print;}' | cut -f6 | sort -rn