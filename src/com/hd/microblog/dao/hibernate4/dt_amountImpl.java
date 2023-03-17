package com.hd.microblog.dao.hibernate4;

import java.util.List;

import org.hibernate.Query;
import org.hibernate.criterion.CriteriaSpecification;
import org.springframework.stereotype.Repository;

import com.hd.common.dao.hibernate4.BaseHibernateDao;
import com.hd.microblog.dao.dt_amountDao;
import com.hd.microblog.model.dt_amount;

@Repository("dt_amountDao")
public class dt_amountImpl extends BaseHibernateDao<dt_amount, Integer>  implements  dt_amountDao{


	

}
