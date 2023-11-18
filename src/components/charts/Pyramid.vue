<script setup>
import { ref, onMounted } from "vue";
import VueApexCharts from "vue3-apexcharts";

const props = defineProps(["chart_config", "activeChart", "series"]);
console.log(props);
const chartOptions = ref({
	series: props.series,
	chart: {
		type: "bar",
		height: 350,
		toolbar: {
			show: false,
		},
		zoom: {
			enabled: false,
		},
	},
	plotOptions: {
		bar: {
			borderRadius: 0,
			horizontal: true,
			distributed: true,
			barHeight: "80%",
			isFunnel: true,
		},
	},
	colors: [
		"#FFFFEE",
		"#FFFFE0",
		"#FAFAD2",
		"#FFFACD",
		"#F5F5DC",
		"#EEE8AA",
		"#F0E68C",
		"#BDB76B",
		"#FFFF00",
		"#FFD700",
		"#DAA520",
		"#B8860B",
	],
	dataLabels: {
		enabled: true,
		formatter: function (val, opt) {
			return opt.w.globals.labels[opt.dataPointIndex];
		},
		dropShadow: {
			enabled: true,
		},
	},
	legend: {
		show: false,
	},
	tooltip: {
		theme: "dark", // 設定主題為 dark
		y: {
			formatter: function (val) {
				return String(val) + String(props.chart_config.unit); // 在提示框中顯示單位
			},
		},
	},
});

const chartRef = ref(null);
</script>

<template>
	<div v-if="activeChart === 'Pyramid'">
		<vue-apex-charts
			:options="chartOptions"
			:series="series"
			type="bar"
			height="350"
		></vue-apex-charts>
	</div>
</template>
