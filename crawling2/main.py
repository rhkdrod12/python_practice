import item_coupang
import time
from item_coupang import itemAciton
from item_coupang import getData
from item_coupang import itemCoupang
from DB import *

if __name__ == '__main__':

    item = itemCoupang()
    item.itemAction.move_url("https://www.coupang.com/vp/products/185502198?itemId=530600312&vendorItemId=4381872911&sourceType=CAMPAIGN&campaignId=82&categoryId=186664&isAddedCart=")

    print(item.getData.Title())
    print(item.getData.Group())