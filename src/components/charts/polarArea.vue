<script setup>
import { ref, onMounted } from "vue";
import VueApexCharts from "vue-apexcharts";

const props = defineProps(["chart_config", "activeChart", "series"]);

const chartOptions = ref({
	series: props.series[0].data.map((item) => item.y),
	chart: {
		type: "polarArea",
	},
	labels: props.series[0].data.map((item) => item.x),
	stroke: {
		colors: ["#fff"],
	},
	fill: {
		opacity: 0.8,
		colors: [
			"#FF5733",
			"#33FF57",
			"#5733FF",
			"#FF5733",
			"#33FF57",
			"#5733FF",
			"#FF5733",
			"#33FF57",
			"#5733FF",
			"#FF5733",
			"#33FF57",
			"#5733FF",
		],
	},
	plotOptions: {
		polarArea: {
			dataLabels: {
				style: {
					colors: ["#FFCCC"], // 設置數據標籤文字顏色
					background: ["#333"], // 設置數據標籤背景色
				},
			},
		},
	},
	legend: {
		show: true,
		position: "right",
		formatter: (seriesName, opts) => {
			return seriesName;
		},
	},
	responsive: [
		{
			breakpoint: 480,
			options: {
				chart: {
					width: 200,
				},
				legend: {
					position: "bottom",
				},
			},
		},
	],
});

const chart = ref(null);

onMounted(() => {
	const options = chartOptions.value;
	chart.value = new ApexCharts(document.querySelector("#chart"), options);
	chart.value.render();
});
</script>

<template>
	<div id="chart" style="width: 100%"></div>
</template>
