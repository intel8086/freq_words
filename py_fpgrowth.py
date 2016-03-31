from pyspark.mllib.fpm import FPGrowth

data = sc.textFile("/home/yinhao/scripts/fp_growth/positive_post.txt")

transactions = data.map(lambda line: line.strip().split(' '))
model = FPGrowth.train(transactions, minSupport=0.01, numPartitions=1)
result = model.freqItemsets().collect()
result_file = open("/home/yinhao/scripts/fp_growth/positive_results.txt",'w+')
for fi in result:
    result_file.write(str(fi))
    result_file.write('\n')

result_file.close()
