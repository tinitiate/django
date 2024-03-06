from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection, connections, transaction

# Import the Model from current APP
from .customer import Customer
from datetime import datetime


#########################################################
# CUSTOM SQL
#########################################################

def sql_getcustomerbyid(request,in_customer_id):

    #cursor = connection['LOANS'].cursor()
    with connections['EMP'].cursor() as cursor:

        cursor.execute("SELECT customer_id, customer_name, application_date, customer_creditscore, customer_req_loanamount FROM customer WHERE customer_id = {}".format(in_customer_id))
        row = cursor.fetchone()
        print(type(row))
    return HttpResponse(row)
###



# Insert THREE rows into customerS table in MySQL database
def sql_createcustomersdata(request):

    with connections['EMP'].cursor() as cursor:
    #
        cursor.execute("insert into customer values(11,'P',now(),251,13445.50);")
        cursor.execute("insert into customer values(22,'Q',now(),133,32500.13);")
        cursor.execute("insert into customer values(33,'R',now(),345,25000.00);")

    connections['EMP'].commit()
        
    return HttpResponse('3 Rows with IDs [11,22,33] Inserted')
###


# Function to Update Salary By EmpID
def sql_updatecustomernamebyid(request, in_customer_id, in_customer_name):

    with connections['EMP'].cursor() as cursor:
    #
        cursor.execute("update customer set customer_name = '{0}' where customer_id = {1};".format(in_customer_name, in_customer_id))

    return HttpResponse("customerID - " + str(in_customer_id) + " updated customer Name " + str(in_customer_name))
###


# Function to Delete Record By EmpID
def sql_deleterecordbyid(request, in_customer_id):

    with connections['EMP'].cursor() as cursor:
    #
        cursor.execute("delete from customer where customer_id = {0};".format(in_customer_id))

    return HttpResponse("customer_id - " + str(in_customer_id) + " deleted")
###


#########################################################
# ORM Object Relational Mapping
#########################################################

# Insert THREE rows into customerS table in MySQL database
def orm_createcustomersdata(request):
    
    """
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=200, blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    customer_creditscore = models.IntegerField(blank=True, null=True)
    customer_req_loanamount = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    """
    # Create customer Object
    # save using the save() method
    CustRec1 = Customer( customer_id   = 111
                        ,customer_name = "AAA111"
                        ,application_date    = datetime.now()
                        ,customer_creditscore = 222
                        ,customer_req_loanamount = 22222.00
                        )

    CustRec1.save()

    CustRec2 = Customer( customer_id   = 222
                        ,customer_name = "BBB222"
                        ,application_date    = datetime.now()
                        ,customer_creditscore = 444
                        ,customer_req_loanamount = 4444.00
                       )

    CustRec2.save()

    CustRec3 = Customer( customer_id   = 333
                        ,customer_name = "CCC333"
                        ,application_date    = datetime.now()
                        ,customer_creditscore = 555
                        ,customer_req_loanamount = 3335.00
                        )

    CustRec3.save()

    return HttpResponse('3 Rows Inserted')
###


# Function to Update Salary By EmpID
def orm_updatecustomernamebyid(request, in_customer_id, in_customer_name):

    rowObj = Customer.objects.get(pk=in_customer_id)
    rowObj.customer_name = in_customer_name

    rowObj.save()

    return HttpResponse("customer ID "+str(in_customer_id)+ " name updated to "+in_customer_name)
###

# Function to Update Salary By EmpID
def orm_updatecustomer_cs(request, in_customer_id, in_customer_cs):

    rowObj = Customer.objects.get(pk=in_customer_id)
    rowObj.customer_creditscore = int(in_customer_cs)

    rowObj.save()

    return HttpResponse("customer ID "+str(in_customer_id)+ " cs updated to "+in_customer_cs)
###

# Function to Update Salary By EmpID
def orm_updatecustomer_amt(request, in_customer_id, in_customer_amt):

    rowObj = Customer.objects.get(pk=in_customer_id)
    rowObj.customer_req_loanamount = float(in_customer_amt)

    rowObj.save()

    return HttpResponse("customer ID "+str(in_customer_id)+ " customer_req_loanamount updated to "+in_customer_amt)
###


# Function to Delete Record By EmpID
def orm_deleterecordbyid(request, in_customer_id):
    #Delete an entry
    rowObj = Customer.objects.get(pk=in_customer_id)
    rowObj.delete()

    return HttpResponse("customer_id - " + str(in_customer_id) + " deleted")
###


# Function to Delete All Records
def orm_deleteallrecords(request):
    data = ""
    for s in Customer.objects.all():
        data = data + str(s.customer_id) + "<br>"
        s.delete()

    return HttpResponse("customer Records deleted for " + "<br>" + data)
###


###
# Get customer Data record by customer_id
def orm_getrecordbyid(request, in_customer_id):

    # Get Row Data by primary key
    rowObj = Customer.objects.get(pk=in_customer_id)

    data = str(rowObj.customer_id) + " " + str(rowObj.customer_name) + " "
    data = data + " " + str(rowObj.application_date)

    return HttpResponse(data)
###


# Method to return all rows from the customer table
def orm_getallrecords(request):
    data = ""
    for s in Customer.objects.all():
        data = data + str(s.customer_id) + " " + str(s.customer_name) + " "
        data = data + " " + str(s.application_date) + " " + "<br>"

    if data == "":
        data = "No Records Found !"

    return HttpResponse(data)
###
