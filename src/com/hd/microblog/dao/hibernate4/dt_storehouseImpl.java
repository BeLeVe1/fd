package com.hd.microblog.dao.hibernate4;


import java.util.List;

import org.hibernate.Query;
import org.hibernate.criterion.CriteriaSpecification;
import org.springframework.stereotype.Repository;

import com.hd.common.dao.hibernate4.BaseHibernateDao;
import com.hd.microblog.dao.dt_storehouseDao;
import com.hd.microblog.model.dt_storehouse;

@Repository("dt_storehouseDao")
public class dt_storehouseImpl extends BaseHibernateDao<dt_storehouse, Integer>  implements  dt_storehouseDao{

}
