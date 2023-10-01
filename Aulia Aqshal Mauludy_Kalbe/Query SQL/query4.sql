select product."Product Name", sum(transaction.totalamount) amount 
from "transaction" full outer join product on transaction.productid  = product.productid 
group by product."Product Name"  
order by amount desc 
limit 1