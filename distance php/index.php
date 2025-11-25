<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <title>محاسبه فاصله</title>
    <link rel="stylesheet" href="style.css">
</head>

<?php
$result = null;
$error = null;

if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $x1 = $_POST['x1'];
    $y1 = $_POST['y1'];
    $x2 = $_POST['x2'];
    $y2 = $_POST['y2'];

    if (!is_numeric($x1) || !is_numeric($y1) || !is_numeric($x2) || !is_numeric($y2)) {
        $error = "لطفاً فقط عدد وارد کنید!";
    } else {

        function distance($x1, $y1, $x2, $y2) {
            return sqrt(pow($x2 - $x1, 2) + pow($y2 - $y1, 2));
        }

        $result = distance($x1, $y1, $x2, $y2);
    }
}
?>

<body>

<div class="container">

    <h2>محاسبه فاصله بین دو نقطه</h2>

    <form method="post">

        <label>مختصات نقطه اول:</label>
        <input type="text" name="x1" placeholder="x1" required>
        <input type="text" name="y1" placeholder="y1" required>

        <label>مختصات نقطه دوم:</label>
        <input type="text" name="x2" placeholder="x2" required>
        <input type="text" name="y2" placeholder="y2" required>
        <br/>
        <button type="submit">محاسبه فاصله</button>
    </form>

    <?php if ($error !== null): ?>
        <div class="error">
            <?= $error ?>
        </div>
    <?php endif; ?>

    <?php if ($result !== null): ?>
        <div class="result">
            فاصله بین دو نقطه: <?= $result ?>
        </div>
    <?php endif; ?>

</div>

</body>
</html>
