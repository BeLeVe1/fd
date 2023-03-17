package com.hd.microblog.web.controller.code;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Date;

import javax.imageio.ImageIO;
import javax.imageio.stream.ImageOutputStream;
import javax.servlet.http.HttpServletRequest;

import org.apache.commons.io.FileUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.multipart.MultipartFile;

public class ImageUtil {
    private final static Logger logger = LoggerFactory.getLogger(ImageUtil.class);

    /**
     * 上传图片的时候，保存文件到本地
     * 
     * @param request
     * @param file
     * @param uploadPath
     *            形如这样的/assets/upload/image/
     * @return /assets/upload/image/abc.jpg
     * @throws IOException
     */
    public static String saveImage(HttpServletRequest request, MultipartFile file, String uploadPath,
    		String realPath) {
        // 如果用的是Tomcat服务器，则文件会上传到\\%TOMCAT_HOME%\\webapps\\YourWebProject\\uploadPath\\文件夹中
        String fileName = file.getOriginalFilename();
        String fileExt[] = fileName.split("\\.");
        String ext = fileExt[fileExt.length - 1];
        logger.debug("-----文件后缀：{}-----", ext);
        if (fileName.equals(ext)) {
            // 未知的文件类型
            logger.error("-----未知的文件类型，文件没有后缀-----");
            return null;
        }
        // String ext = file.getContentType().split("\\/")[1];
        //生成文件名
        int sjcode = (int) (Math.random()*9000+1000);
		String order_code = String.valueOf(System.currentTimeMillis() / 1000)+sjcode;
        String newFileName = order_code + "." + ext;
        System.out.println(realPath);
        /*String filePathAndName = null;
        if (realPath.endsWith(File.separator)) {
            filePathAndName = realPath + newFileName;
        } else {
            filePathAndName = realPath + File.separator + newFileName;
        }
        logger.info("-----上传的文件:{}-----", filePathAndName);*/
        try {
            // 先把文件保存到本地
            FileUtils.copyInputStreamToFile(file.getInputStream(), new File(uploadPath, newFileName));
        } catch (Exception e) {
        	e.printStackTrace();
        }
        // 然后进行压缩处理
        /*thumbImage(filePathAndName);*/
        //return realPath + newFileName;
        return newFileName;
    }

    /**
     * 删除文件
     * 
     * @param request
     * @param filePath
     * @return
     */
    /*public static boolean deleteFile(HttpServletRequest request, String filePath) {

        String realPath = request.getSession().getServletContext().getRealPath(filePath);
        logger.info("-----要删除文件的路径:{}-----", realPath);
        File file = new File(realPath);
        try {
            FileUtils.forceDelete(file);
            return true;
        } catch (IOException e) {
            logger.info("-----删除图片发生异常:{}-----", e.getMessage());
            return false;
        }

    }*/

    /**
     * 图片压缩 大于2M的0.5压缩比 小于1M的0.8压缩比
     * 
     * @param imageRealPath
     *            图片在磁盘的绝对路径，比如C:\\file.jpg
     */
    /*public static void thumbImage(String imageRealPath) {
        File file = new File(imageRealPath);
        if (file.length() >= 1024 * 1024 * 2) {
            thumbImage(imageRealPath, 0.5);
        } else if (file.length() < 1024 * 1024 * 2 && file.length() >= 1024 * 1024 * 1) {
            thumbImage(imageRealPath, 0.8);
        } else {
            thumbImage(imageRealPath, 1);
        }

    }

    public static void thumbImage(String imageRealPath, double size) {
        logger.info("进行图片压缩，路径:{},比例:{}",imageRealPath,size);
        if(size-1==0){
            return;
        }
        try {
            Thumbnails.of(imageRealPath).scale(size).toFile(imageRealPath);
        } catch (IOException e) {
            logger.error("-----读取图片发生异常:{}-----", e.getMessage());
            logger.info("-----尝试cmyk转化-----");
            File cmykJPEGFile = new File(imageRealPath);
            try {
                BufferedImage image = ImageIO.read(cmykJPEGFile);
                ImageOutputStream output = ImageIO.createImageOutputStream(cmykJPEGFile);
                if (!ImageIO.write(image, "jpg", output)) {
                    logger.info("-----cmyk转化异常:{}-----");
                }
                Thumbnails.of(image).scale(0.4f).toFile(imageRealPath);
                logger.info("-----cmyk转化成功-----");
            } catch (IOException e1) {
                logger.info("-----cmyk转化异常:{}-----", e1.getMessage());
            }
        }
    }*/

}