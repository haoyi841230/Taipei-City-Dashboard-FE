<script setup>
import { ref, onMounted, watchEffect, defineProps } from "vue";
import VueApexCharts from "vue-apexcharts";

const { chart_config, activeChart, series } = defineProps([
	"chart_config",
	"activeChart",
	"series",
]);

const chartOptions = ref({
	series: series[0].data.map((item) => item.y),
	chart: {
		type: "polarArea",
	},
	labels: series[0].data.map((item) => item.x),
	colors: series[0].data.map((item) => item.z),
	stroke: {
		colors: ["#000"],
	},
	fill: {
		opacity: 0.8,
		colors: [
			"#006400",
			"#228B22",
			"#2E8B57",
			"#008080",
			"#20B2AA",
			"#66CDAA",
			"#3CB371",
			"#8FBC8F",
			"#9ACD32",
			"#32CD32",
			"#00FF00",
			"#7FFF00",
		],
	},
	plotOptions: {
		polarArea: {
			dataLabels: {
				style: {
					colors: ["#FFCCC"],
					background: ["#333"],
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

const chartEl = ref(null);

onMounted(() => {
	const options = chartOptions.value;
	chartEl.value = new ApexCharts(document.querySelector("#chart"), options);
	chartEl.value.render();
});

// 監聽 series 的變化
watchEffect(() => {
	console.log(series[0].data.map((item) => item.z));
	if (chartEl.value) {
		// 如果 chart 已經初始化，則更新圖表
		chartEl.value.updateOptions({
			series: series[0].data.map((item) => item.y),
			labels: series[0].data.map((item) => item.x),
			colors: [
				"#006400",
				"#228B22",
				"#2E8B57",
				"#008080",
				"#20B2AA",
				"#66CDAA",
				"#3CB371",
				"#8FBC8F",
				"#9ACD32",
				"#32CD32",
				"#00FF00",
				"#7FFF00",
			],
		});
	}
});
</script>

<template>
	<div v-if="activeChart === 'polarArea'">
		<div id="chart" style="width: 100%" ref="chartEl"></div>
	</div>
</template>
