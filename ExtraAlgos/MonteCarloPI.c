#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


//Generate random long double number between the given boundries
long double doublRand(long double min, long double max) {
    long double range = (max - min);
    long double rnd = RAND_MAX / range;
    return min + (rand() / rnd);
}

//Generate random point in the given bounds
long double * genPoint(long double lowerBound, long double higherBound, long double min, long double max, long double * result){
	long double x = doublRand(lowerBound, higherBound);
	long double y = doublRand(min, max);
	result[0] = x;
	result[1] = y;
	return result;
}

//Return true if a point is inside of a circle with center in [0, 0] and given diameter
bool isInCircle(long double * point, long double diameter){
	if ((point[0] * point[0])+(point[1] * point[1]) <= (diameter*diameter)){
		return true;
	}
	return false;
}

//Use given accuracy to approximate the value of pi
long double aproxPi(size_t accuracy){
	size_t in = 0;

	for (size_t i = 0; i < accuracy; i++){
		long double point[2];
		genPoint(-10, 10, -10, 10, point);
		isInCircle(point, 10) ? in++ : in;
	}

	return (4)/(accuracy/(long double)in);
}

int main(int argc, char const *argv[])
{
	for (register size_t i = 10; i <= 1000000000; i *= 10){
		printf("Used %ld points, PI - %Lf\n", i,aproxPi(i));
	}

	return 0;
}