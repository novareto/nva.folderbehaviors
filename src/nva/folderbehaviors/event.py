from DateTime import DateTime
from datetime import date
from dateutil.relativedelta import relativedelta
import random
from time import strftime, localtime
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName

def newsExpiration(obj, event):
    if obj.portal_type == 'News Item':
        heute = date.today()
        year1 = heute + relativedelta(years=+1)
        obj.setExpirationDate(DateTime(str(year1)))
