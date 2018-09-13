#/bin/bash

# LOAD THE PYTHON 3.5 MODULE
module load python/3.5.2

# GET MATRIX SIZE ARGUMENT IF SET
if [ "$#" -eq 1 ]; then
   MAT_DIM=$1
else
   MAT_DIM=1000
fi

# SET NUMBER OF THREADS TO 1 -- ALLOW NUMPY TO USE ONLY ONE CORE
export OMP_NUM_THREADS=1
echo ""
echo "RUNNING dotprod.py FOR MATRIX OF SIZE: [ $MAT_DIM x $MAT_DIM ] WITH $OMP_NUM_THREADS THREADS"
python dotprod.py $MAT_DIM
echo ""

# SET NUMBER OF THREADS TO 4 -- ALLOW NUMPY TO USE 4 CORES
export OMP_NUM_THREADS=4
echo ""
echo "RUNNING dotprod.py FOR MATRIX OF SIZE: [ $MAT_DIM x $MAT_DIM ] WITH $OMP_NUM_THREADS THREADS"
python dotprod.py $MAT_DIM
echo ""
