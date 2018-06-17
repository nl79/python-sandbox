$mean = 0;
$alg = shift;
$data = shift;

$dir=$data;

$mean = 0;
for(my $i=0; $i<10; $i++){
  system("python3 $alg.py $dir/$data.data $dir/$data.trainlabels.$i > $alg.out.$data");
  $err[$i] = `perl error.pl $dir/$data.labels $alg.out.$data`;
  chomp $err[$i];
  print "$err[$i]\n";
  $mean += $err[$i];
}
$mean /= 10;
$sd = 0;
for(my $i=0; $i<10; $i++){
  $sd += ($err[$i]-$mean)**2;
}

$sd /= 10;
$sd = sqrt($sd);
print "$alg error = $mean ($sd)\n";
