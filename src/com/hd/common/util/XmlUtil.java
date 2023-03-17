package com.hd.common.util;

import com.thoughtworks.xstream.XStream;

/**
 * User: rizenguo
 * Date: 2014/10/23
 * Time: 14:59
 */
public class XmlUtil {

	public static Object getObjectFromXML(String xml, Class tClass) {
        //将从API返回的XML数据映射到Java对象
        XStream xStreamForResponseData = new XStream();
       // XStream xStreamForResponseData = new XStream(new XppDriver(new XmlFriendlyReplacer("_-", "_")));
        xStreamForResponseData.alias("xml", tClass);
        xStreamForResponseData.ignoreUnknownElements();//暂时忽略掉一些新增的字段
        return xStreamForResponseData.fromXML(xml);
    }

}

