<?php
$result = null;
$error = null;

if (
    isset($_GET['x1']) && isset($_GET['y1']) &&
    isset($_GET['x2']) && isset($_GET['y2'])
) {
    $x1 = $_GET['x1'];
    $y1 = $_GET['y1'];
    $x2 = $_GET['x2'];
    $y2 = $_GET['y2'];

    // بررسی عددی بودن
    if (!is_numeric($x1) || !is_numeric($y1) || !is_numeric($x2) || !is_numeric($y2)) {
        $error = "خطا: لطفاً فقط عدد وارد کنید.";
    } else {
        $result = sqrt(pow($x2 - $x1, 2) + pow($y2 - $y1, 2));
    }
} else {
    $error = "مختصات در URL ارسال نشده‌اند!";
}
?>

<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <title>نتیجه محاسبه</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">

    <h2>نتیجه محاسبه فاصله</h2>

    <?php if ($error): ?>
        <div class="error"><?= $error ?></div>
    <?php endif; ?>

    <?php if ($result !== null): ?>
        <div class="result">فاصله بین دو نقطه: <?= $result ?></div>
    <?php endif; ?>

    <a href="index.html">
        <button style="margin-top: 15px;">بازگشت</button>
    </a>

</div>

</body>
</html>
