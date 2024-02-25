const puppeteer = require('puppeteer');

async function generatePDF(url, outputPath) {

    // 启动浏览器
    const browser = await puppeteer.launch({ headless: false });

    try {
        // ...
        // 创建一个新的页面
        const page = await browser.newPage();

        // 访问指定URL
        await page.goto(url, { waitUntil: 'networkidle2' }); // 等待网络空闲，确保所有资源加载完成

        // // 将页面滚动到底部，触发懒加载内容加载（如果存在）
        // await page.evaluate(() => new Promise((resolve, _) => {
        //     window.scroll(0, document.body.scrollHeight);
        //     setTimeout(resolve, 2000); // 调整延时以适应不同网页的加载速度
        // }));

        await scrollAndWaitForHtmlStaleness(page);

        // 将页面内容渲染为PDF
        await page.pdf({
            path: outputPath, // PDF输出路径
            format: 'A4', // 页面大小，默认为Letter格式
            printBackground: true, // 是否包含背景色和图片
            margin: { top: '1cm', right: '1cm', bottom: '1cm', left: '1cm' }, // 边距
            preferCSSPageSize: true // 是否优先使用CSS定义的页面尺寸
        });

        // 关闭浏览器
        await browser.close();

    } catch (error) {
        console.error('An error occurred:', error);
    } finally {
        // 确保无论成功与否都关闭浏览器
        await browser.close();
    }

}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function scrollAndWaitForHtmlStaleness(page, timeoutInSeconds = 30) {
    let height = await page.evaluate(() => document.documentElement.scrollHeight);
    let k = 0;

    while (k * 500 < height) {
        const jsMove = `window.scrollTo(0, ${k * 500})`;
        console.log(jsMove);
        await page.evaluate(jsMove);
        // await page.waitForTimeout(500); // 等待0.5秒
        await sleep(500);
        height = await page.evaluate(() => document.documentElement.scrollHeight);
        k += 1;
    }
}

// 获取命令行参数
const args = process.argv.slice(2); // 忽略掉 'node' 和脚本名

console.log('Received arguments:');
args.forEach((arg, index) => {
    console.log(`Argument #${index + 1}: ${arg}`);
});

console.log(args[0])
console.log(args[1])

// 使用函数



generatePDF(args[0], args[1])
    .then(() => console.log('PDF generated successfully'))
    .catch(error => console.error('Failed to generate PDF:', error));