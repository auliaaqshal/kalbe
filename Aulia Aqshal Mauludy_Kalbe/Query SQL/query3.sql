select store.storename, sum(transaction.qty) quantity 
from "transaction" full outer join store on transaction.storeid = store.storeid 
group by store.storename 
order by quantity desc 
limit 1  