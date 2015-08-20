import pyspark

def vowel_mapper(line):
    key_value_pairs = []
    for vowel in 'aeiou':
        count = line.count(vowel)
        if count > 0:
            key_value_pairs.append((vowel, count))
    return key_value_pairs

def vowel_reducer(values):
    return sum(values)

spark_context = pyspark.SparkContext('local[2]', 'CountVowels')
text_file = spark_context.textFile('reviews.json')

vowel_counts = text_file.flatMap(vowel_mapper)    \
                        .groupByKey()             \
                        .mapValues(vowel_reducer)

for vowel, counts in vowel_counts.collect():
    print(vowel, counts)
