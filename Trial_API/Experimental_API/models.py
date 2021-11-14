from django.db import models
'''
        Advisor Table                                       User Table                                      Booking Table     
*******************************     ***********************************************************   ****************************
* Adv Id * Adv Name * Adv pic *     * user id * user name * user email *user password * bk id *   * bk id * bk time * Adv id *
*******************************     ***********************************************************   ****************************
*        *          *         *     *         *           *            *              *       *   *       *         *        *
*        *          *         *     *         *           *            *              *       *   *       *         *        *
*        *          *         *     *         *           *            *              *       *   *       *         *        *
*******************************     ***********************************************************   ****************************

'''
# Create your models here.

class Advisor(models.Model):
    Advisor_id=models.CharField(max_length=100)
    Advisor_name=models.CharField(max_length=100)
    Advisor_picture_url=models.CharField(max_length=100)

class User(models.Model):
    user_id=models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    user_email=models.CharField(max_length=100)    
    user_password=models.CharField(max_length=200)
class Booking(models.Model):
    Booking_id=models.CharField(max_length=100)
    Booking_time=models.CharField(max_length=100)
    Advisor_id=models.ForeignKey(Advisor,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)