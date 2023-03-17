package com.hd.microblog.util;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;  
import java.io.IOException;  
import java.io.InputStream;  
import java.io.OutputStream;  

import sun.misc.BASE64Decoder;  
import sun.misc.BASE64Encoder;  
public class Base64Test   
{  
	public static boolean base64StrToImage(String imgStr, String path) {
		   if (imgStr == null)
		   return false;
		   BASE64Decoder decoder = new BASE64Decoder();
		   try {
		     // 解密
		     byte[] b = decoder.decodeBuffer(imgStr);
		     // 处理数据
		     for (int i = 0; i < b.length; ++i) {
		       if (b[i] < 0) {
		         b[i] += 256;
		       }
		     }
		     //文件夹不存在则自动创建
		     File tempFile = new File(path);
		     if (!tempFile.getParentFile().exists()) {
		       tempFile.getParentFile().mkdirs();
		     }
		     OutputStream out = new FileOutputStream(tempFile);
		     out.write(b);
		     out.flush();
		     out.close();
		     return true;
		   } catch (Exception e) {
			   e.printStackTrace();
		     return false;
		   }
		 }

 
}