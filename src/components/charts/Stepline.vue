<script setup>
import { ref, defineProps, onMounted } from "vue";
import VueApexCharts from "vue3-apexcharts";

const props = defineProps(["chart_config", "activeChart", "series"]);
console.warn("props", props);
const chartOptions = ref({
	chart: {
		type: "line",
		height: 350,
		toolbar: {
			show: false,
		},
		zoom: {
			enabled: false,
		},
	},
	stroke: {
		curve: "stepline",
	},
	dataLabels: {
		enabled: false,
	},
	colors: props.chart_config.color,
	markers: {
		hover: {
			sizeOffset: 4,
		},
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

onMounted(() => {
	// Access the chart instance using chartRef.value if needed
});
</script>

<template>
	<div v-if="activeChart === 'Stepline'">
		<vue-apex-charts
			:options="chartOptions"
			:series="series"
			type="line"
		></vue-apex-charts>
	</div>
</template>
