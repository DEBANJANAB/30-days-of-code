int main(){
    int totalcost=0;
    float mealcost,tip,tax;
    
    scanf("%f%f%f",&mealcost,&tip,&tax);
    tip=tip*mealcost/100;
    tax=tax*mealcost/100;
    totalcost=mealcost+tip+tax;
    printf("%d",(int)(round(totalcost)));
}
