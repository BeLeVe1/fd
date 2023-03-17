package com.hd.microblog.dao.hibernate4;

import java.util.List;

import org.hibernate.Query;
import org.hibernate.criterion.CriteriaSpecification;
import org.springframework.stereotype.Repository;

import com.hd.common.dao.hibernate4.BaseHibernateDao;
import com.hd.microblog.dao.dt_predictionDao;
import com.hd.microblog.model.dt_prediction;

@Repository("dt_predictionDao")
public class dt_predictionImpl extends BaseHibernateDao<dt_prediction, Integer>  implements  dt_predictionDao{


	

}
